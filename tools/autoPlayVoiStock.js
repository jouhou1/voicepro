/*
右上の三点＞ブックマーク＞ブックマークマネージャを開き、そのページの右上の三点から新しいブックマークを追加する。
URLの欄に次のコードをコピペする。

javascript:(async()=>{for(let e of $(".playgroup")){e=$(e);e.click();while(e.hasClass("fa-pause")){await new Promise(r => setTimeout(r, 500))}}})()

VoiStockのページ（https://www.voistock.com/ja/voicelist/index.php）でブックマークを押すと
画面に出ている音声データを上から順に自動再生できる。pキーで一時停止・再開、sキーで停止。
（DevToolsのコンソールからも使える）
以下は最適化前のコード
*/

const sleep = waitTime => new Promise(resolve => setTimeout(resolve, waitTime));

let pause = false;
let stop = false;
$(document).off("keydown.app")
$(document).on("keydown.app", (event) => {
    switch (event.key) {
        case "p":
            pause = !pause;
            break;
        case "s":
            stop = true;
            break;
    }
})

(async () => {
for (let elem of $(".playgroup")) {
    elem = $(elem);
    elem.click();
    while (elem.hasClass("fa-pause")) {
        if (stop) return;
        if (pause) {
            while (true) {
                if (!pause) break;
                sleep(500);
            }
            elem.click();
        }
        await sleep(500);
    };
}
})()
