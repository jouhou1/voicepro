/*
右上の三点＞ブックマーク＞ブックマークマネージャを開き、そのページの右上の三点から新しいブックマークを追加する。
URLの欄に次のコードをコピペする。

javascript:(async()=>{for(let e of $(".playgroup")){e=$(e);e.click();while(e.hasClass("fa-pause")){await new Promise(r => setTimeout(r, 500))}}})()

VoiStockのページ（https://www.voistock.com/ja/voicelist/index.php）
画面に出ている音声データを自動で上から順に再生してくれます。
（DevToolsのコンソールからも使えます）
以下は最適化前のコード
*/

const sleep = waitTime => new Promise(resolve => setTimeout(resolve, waitTime));

(async () => {
for (let elem of $(".playgroup")) {
    elem = $(elem);
    elem.click();
    while (elem.hasClass("fa-pause")) {
        await sleep(500);
        
    };
}})()
