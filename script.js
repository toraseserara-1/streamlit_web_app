function calculateSquare() {
    // ユーザーが入力した数値を取得
    var numberInput = document.getElementById("numberInput").value;

    // サーバーにリクエストを送信し、結果を取得
    fetch(`/square?number=${numberInput}`)
        .then(response => response.json())
        .then(data => {
            // 結果を表示
            document.getElementById("result").innerHTML = `Square: ${data.square}`;
        })
        .catch(error => console.error('Error:', error));
}