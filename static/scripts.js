function copyToClipboard() {
    var copyText = document.getElementById("replyBox");

    var range = document.createRange();
    range.selectNode(copyText);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);

    document.execCommand("copy");

    var copyButton = document.getElementById("copyButton");
    copyButton.textContent = "Copied to Clipboard!";

    setTimeout(function () {
        copyButton.textContent = "Copy Reply";
    }, 5000);
}

document.getElementById("copyButton").addEventListener("click", copyToClipboard);