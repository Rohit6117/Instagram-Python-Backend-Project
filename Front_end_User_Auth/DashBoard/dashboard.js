const fileInput = document.getElementById("fileInput");
const feed = document.getElementById("feed");

function openFile() {
    fileInput.click();
}

fileInput.addEventListener("change", () => {
    const files = Array.from(fileInput.files);
    if (!files.length) return;

    const post = document.createElement("div");
    post.className = "post";

    const imagesHTML = files.map(file => {
        const url = URL.createObjectURL(file);
        return `<img src="${url}" />`;
    }).join("");

    post.innerHTML = `
        <div class="post-header">
            <img src="https://i.pravatar.cc/150?img=3">
            <strong>rohit_patil</strong>
        </div>

        <div class="carousel">
            ${imagesHTML}
        </div>

        <div class="post-actions">
            <i class="fa-regular fa-heart" onclick="likePost(this)"></i>
            <i class="fa-regular fa-comment"></i>
            <i class="fa-regular fa-paper-plane"></i>
        </div>

        <div class="likes">0 likes</div>

        <div class="caption">
            <span>rohit_patil</span> New post 🔥
        </div>
    `;

    feed.prepend(post);
    fileInput.value = "";
});

function likePost(icon) {
    const likesDiv = icon.parentElement.nextElementSibling;
    let likes = parseInt(likesDiv.textContent);

    if (icon.classList.contains("fa-regular")) {
        icon.classList.replace("fa-regular", "fa-solid");
        icon.style.color = "red";
        likes++;
    } else {
        icon.classList.replace("fa-solid", "fa-regular");
        icon.style.color = "black";
        likes--;
    }

    likesDiv.textContent = `${likes} likes`;
}
