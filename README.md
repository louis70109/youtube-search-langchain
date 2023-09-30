## LangChain Example for Youtube search

使用 LangChain 搭配 OpenAI，當呼叫 API 時提供問題，則會回傳一個影片以及敘述給用戶

## 環境變數

你需要設置以下環境變數：

- API_ENV: 應用程式的運行環境，可以是 'production' 或 'develop'，預設 develop。
- LOG: 紀錄的等級，例如 'WARNING'、'INFO'、'DEBUG' 等。
- OPENAI_API_KEY: OpenAI 的 API Key。
- PORT: 預設 8080


## 使用方法

```
git clone https://github.com/louis70109/calendar-linebot
cd calendar-linebot/
pip install -r requirements.txt
# python3 -m venv venv; source venv/bin/activate # 如果有的話
python main.py
```

## Google Cloud Platform 佈署

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

Clone 此專案

```
git clone https://github.com/louis70109/calendar-linebot
cd calendar-linebot/
```

### gcloud 基礎設定

- `gcloud init`：初始化 gcloud CLI，該指令會提示登錄 Google 帳戶，並選擇您要使用的 GCP 項目。
- `gcloud config set project PROJECT_ID`：設定 GCP Project ID，以便 gcloud CLI 與該項目交互使用。
- `gcloud auth login`：登錄 Google 帳戶。

透過 [gcloud](https://cloud.google.com/sdk/docs/install?hl=zh-cn) 指令佈署

```
gcloud run deploy calendar-linebot-1 --source .
```

> 佈署參考: [【GCP】將 FastAPI 佈署上 Cloud Run](https://nijialin.com/2023/03/19/gcp-why-need-cloudrun-as-serverless/#5-%E4%BD%88%E7%BD%B2%E5%88%B0-Google-Cloud-Run)

## 參與貢獻

如果你有任何問題或建議，歡迎開 issue 或 pull request。

## LISENSE

[MIT](https://github.com/louis70109/youtube-search-langchain/blob/main/LICENSE)