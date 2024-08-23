// ホバーボタンのJavaScript例
document.addEventListener('DOMContentLoaded', function() {
    // ボタン要素を取得
    var button = document.getElementById('hover-button');

    // ホバー時の動作を追加
    button.addEventListener('mouseover', function() {
        // ホバー時のアクションをここに追加
        console.log('ボタンにホバーしています！');
        // 他のアクションを追加したい場合はここに記述
    });

    // ホバーから外れた時の動作を追加
    button.addEventListener('mouseout', function() {
        // ホバーから外れた時のアクションをここに追加
        console.log('ボタンから外れました。');
        // 他のアクションを追加したい場合はここに記述
    });
});
