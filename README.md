# 使い方
`setup.sh`はEC2(Amazon Linux 2)での利用を想定としています。
Docker環境の構築を手動で行えば、UbuntuやCentOSなどでも利用できます。

1. `setup.sh`を実行
2. `.env.template`ファイルに従って`.env`ファイルを作成
2. `docker compose up -d`を実行