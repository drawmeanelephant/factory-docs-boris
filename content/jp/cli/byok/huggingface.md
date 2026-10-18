---
id: jp/cli/byok/huggingface
title: "Hugging Face"
status: published
summary: "Hugging FaceのInference Providersでホストされているモデルに接続する"
parent: jp/cli/byok/index
tags: [cli, huggingface, hugging-face, api-key, byok, inference, custom-model, open-source]
relations: [relates_to=cli/byok/huggingface]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Hugging Face</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Hugging FaceのInference Providersでホストされているモデルに接続する</p>


Hugging Faceの推論プロバイダーでホストされている数千のモデルに接続できます。詳細は[Inference Providers documentation](https://huggingface.co/docs/inference-providers/en/index)をご覧ください。



<Aside kind="note">
**モデルパフォーマンス**: 300億パラメータ未満のモデルは、エージェント型コーディングタスクで大幅に低い性能を示しています。HuggingFaceには実験に役立つ小型モデルが多数ありますが、本番のコーディング作業には一般的に推奨されません。複雑なソフトウェアエンジニアリングタスクには300億以上のパラメータを持つモデルの使用を検討してください。
</Aside>



## 設定 {#configuration}

`~/.factory/settings.json`に追加してください：

```json
{
  "customModels": [
    {
      "model": "openai/gpt-oss-120b:fireworks-ai",
      "displayName": "GPT OSS 120B [HF Router]",
      "baseUrl": "https://router.huggingface.co/v1",
      "apiKey": "YOUR_HF_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32768
    },
    {
      "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct:fireworks-ai",
      "displayName": "Llama 4 Scout 17B [HF Router]",
      "baseUrl": "https://router.huggingface.co/v1",
      "apiKey": "YOUR_HF_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    }
  ]
}
```

## はじめに {#getting-started}

1. [huggingface.co](https://huggingface.co)でサインアップしてください
2. [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)からトークンを取得してください
3. [huggingface.co/models](https://huggingface.co/models?pipeline_tag=text-generation&inference_provider=all&sort=trending)でモデルを閲覧してください
4. 希望するモデルを設定に追加してください

## 注意事項 {#notes}

- モデル名は正確なHugging Faceリポジトリ IDと一致する必要があります
- 一部のモデルはHFウェブサイトで最初にライセンス契約に同意する必要があります
- 大きなモデルは無料ティアでは利用できない場合があります
