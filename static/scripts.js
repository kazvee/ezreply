document.addEventListener("DOMContentLoaded", function() {
    function setupCopyButton() {
        var copyButton = document.getElementById("copyButton");
        var replyBox = document.getElementById("replyBox");

        if (copyButton && replyBox) {
            copyButton.addEventListener("click", function() {
                var range = document.createRange();
                range.selectNode(replyBox);
                window.getSelection().removeAllRanges();
                window.getSelection().addRange(range);

                document.execCommand("copy");

                copyButton.textContent = "Copied to Clipboard!";

                setTimeout(function() {
                    copyButton.textContent = "Copy Reply";
                }, 5000);
            });
        }
    }

    var isReplySelected = document.getElementById('replyBox');
    if (isReplySelected) {
        setupCopyButton();
    }
});