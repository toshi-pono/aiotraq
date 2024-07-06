---
id: bot-event
title: BOT イベント
sidebar_label: BOT Event
---

このページでは、traQ Bot が受け取ることができるイベントの一覧を紹介します。

:::note
各イベントの詳細は traQ BOT Console のイベントリファレンスを参照してください。

BOT の権限一覧は [ソース](https://github.com/traPtitech/traQ/blob/master/service/rbac/role/bot.go)から確認できます。
:::

## イベント一覧

| イベント文字列               | 型ヒント                         | 説明                                                     |
| ---------------------------- | -------------------------------- | -------------------------------------------------------- |
| `PING`                       | `PingPayload`                    | 疎通確認イベント。BOT は自動で 204 を返します            |
| `JOINED`                     | `JoinedPayload`                  | BOT がチャンネルに参加した                               |
| `LEFT`                       | `LeftPayload`                    | BOT がチャンネルから退出した                             |
| `MESSAGE_CREATED`            | `MessageCreatedPayload`          | チャンネルにメッセージが投稿された                       |
| `MESSAGE_UPDATED`            | `MessageUpdatedPayload`          | チャンネルのメッセージが編集された                       |
| `MESSAGE_DELETED`            | `MessageDeletedPayload`          | チャンネルのメッセージが削除された                       |
| `DIRECT_MESSAGE_CREATED`     | `DirectMessageCreatedPayload`    | BOT に対してダイレクトメッセージが投稿された             |
| `DIRECT_MESSAGE_UPDATED`     | `DirectMessageUpdatedPayload`    | BOT に対してのダイレクトメッセージが編集された           |
| `DIRECT_MESSAGE_DELETED`     | `DirectMessageDeletedPayload`    | BOT に対してのダイレクトメッセージが削除された           |
| `BOT_MESSAGE_STAMPS_UPDATED` | `BotMessageStampsUpdatedPayload` | BOT が投稿したメッセージに押されているスタンプが変化した |
| `CHANNEL_CREATED`            | `ChannelCreatedPayload`          | チャンネルが作成された                                   |
| `CHANNEL_TOPIC_CHANGED`      | `ChannelTopicChangedPayload`     | チャンネルのトピックが変更された                         |
| `USER_CREATED`               | `UserCreatedPayload`             | ユーザーが作成された                                     |
| `USER_ACTIVATED`             | `UserActivatedPayload`           | ユーザーが凍結解除された                                 |
| `STAMP_CREATED`              | `StampCreatedPayload`            | スタンプが作成された                                     |
| `TAG_ADDED`                  | `TagAddedPayload`                | BOT にタグが追加された                                   |
| `TAG_REMOVED`                | `TagRemovedPayload`              | BOT からタグが削除された                                 |
| `USER_GROUP_CREATED`         | `UserGroupCreatedPayload`        | ユーザーグループが作成された                             |
| `USER_GROUP_UPDATED`         | `UserGroupUpdatedPayload`        | ユーザーグループが更新された                             |
| `USER_GROUP_DELETED`         | `UserGroupDeletedPayload`        | ユーザーグループが削除された                             |
| `USER_GROUP_MEMBER_ADDED`    | `UserGroupMemberAddedPayload`    | ユーザーグループにメンバーが追加された                   |
| `USER_GROUP_MEMBER_UPDATED`  | `UserGroupMemberUpdatedPayload`  | ユーザーグループのメンバーが更新された                   |
| `USER_GROUP_MEMBER_REMOVED`  | `UserGroupMemberRemovedPayload`  | ユーザーグループのメンバーが削除された                   |
| `USER_GROUP_ADMIN_ADDED`     | `UserGroupAdminAddedPayload`     | ユーザーグループに管理者が追加された                     |
| `USER_GROUP_ADMIN_REMOVED`   | `UserGroupAdminRemovedPayload`   | ユーザーグループから管理者が削除された                   |

:::tip
BotMessageStampsUpdatedPayload: このイベントは traQ 側で１秒間スロットリングされます。イベントペイロードの stamps はその時点でメッセージに押されている全てのスタンプの配列です。詳細は BOT Console のイベントリファレンスを参照してください。
:::
