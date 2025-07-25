import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "AiotraQ",
  tagline: "API Client & BOT Library for traQ",
  favicon: "img/favicon.svg",

  // Set the production url of your site here
  url: "https://toshi-pono.github.io",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/aiotraq/",
  trailingSlash: true,

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "toshi-pono", // Usually your GitHub org/user name.
  projectName: "aiotraq", // Usually your repo name.

  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "ja",
    locales: ["ja"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: "https://github.com/toshi-pono/aiotraq/tree/main/docs/",
          admonitions: {
            keywords: ["border"],
            extendDefaults: true,
          },
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: "img/ogp.png",
    metadata: [
      { name: "keywords", content: "traQ, API, Client, Library, Bot, AiotraQ" },
      { name: "og:title", content: "AiotraQ" },
      { name: "og:description", content: "API Client & BOT Library for traQ" },
      {
        name: "og:image",
        content: "https://toshi-pono.github.io/aiotraq/img/ogp.png",
      },
      { name: "og:url", content: "https://toshi-pono.github.io/aiotraq/" },
      { name: "og:type", content: "website" },
      { name: "author", content: "toshi-pono" },
    ],
    navbar: {
      title: "AiotraQ",
      logo: {
        alt: "AiotraQ Logo",
        src: "img/aiotraq.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Docs",
        },
        {
          href: "https://github.com/toshi-pono/aiotraq",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "light",
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Tutorial",
              to: "/docs/intro",
            },
          ],
        },
        {
          title: "GitHub",
          items: [
            {
              label: "Repository",
              href: "https://github.com/toshi-pono/aiotraq",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "Digital Creators Club traP",
              href: "https://trap.jp/",
            },
            {
              label: "traQ",
              href: "https://github.com/traPtitech/traQ",
            },
          ],
        },
      ],
      copyright: `Created by toshi-pono ${new Date().getFullYear()}`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
    algolia: {
      // The application ID provided by Algolia
      appId: "SIH9ECXQ07",

      // Public API key: it is safe to commit it
      apiKey: "63ed4c0dbeb099b5ce32462d2747dc6b",

      indexName: "toshi-ponoio",

      // Optional: see doc section below
      contextualSearch: true,

      // Optional: path for search page that enabled by default (`false` to disable it)
      searchPagePath: "search",

      // Optional: whether the insights feature is enabled or not on Docsearch (`false` by default)
      insights: false,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
