$(document).ready(() => {
    $(".chat-btn").click(() => {
        $(".chat-box").slideToggle("slow")
    })
})

function loadLink(event) {
    event.preventDefault();
    const displayDiv = document.getElementById('display');
    const amazonLink = event.target.href;
    displayDiv.innerHTML = `<iframe src="${amazonLink}" frameborder="0"></iframe>`;
  }