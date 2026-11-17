// Exercise the APIs used by upstream parents across the temporary major overrides.
const assert = require('node:assert/strict');
const { mkdtemp, writeFile, rm } = require('node:fs/promises');
const { createRequire } = require('node:module');
const { tmpdir } = require('node:os');
const { join } = require('node:path');
const { test } = require('node:test');
const { pathToFileURL } = require('node:url');

test('Docusaurus worker options, context, and task execution', async () => {
  const parentRequire = createRequire(require.resolve('@docusaurus/core/package.json'));
  const { default: Tinypool } = await import(pathToFileURL(parentRequire.resolve('tinypool')));
  const directory = await mkdtemp(join(tmpdir(), 'aiotraq-tinypool-'));
  let pool;
  try {
    const filename = join(directory, 'worker.cjs');
    await writeFile(filename, `
      const { workerData } = require('node:worker_threads');
      module.exports = task => ({
        task,
        params: workerData[1].params,
        hasWorkerId: Boolean(process.__tinypool_state__.workerId),
      });
    `);
    pool = new Tinypool({
      filename,
      minThreads: 2,
      maxThreads: 2,
      concurrentTasksPerWorker: 1,
      runtime: 'worker_threads',
      isolateWorkers: false,
      workerData: { params: { site: 'aiotraq' } },
    });
    assert.deepEqual(await pool.run({ pathnames: ['/docs/intro/'] }), {
      task: { pathnames: ['/docs/intro/'] },
      params: { site: 'aiotraq' },
      hasWorkerId: true,
    });
  } finally {
    await pool?.destroy();
    await rm(directory, { recursive: true, force: true });
  }
});

test('SockJS can use the CommonJS uuid.v4 API', () => {
  const parentRequire = createRequire(require.resolve('sockjs'));
  assert.match(parentRequire('uuid').v4(), /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/);
  assert.equal(typeof require('sockjs').createServer().installHandlers, 'function');
});
