function showPopup() {
    const popup = document.getElementById("bottom_popup");
    popup.classList.add("show");
    setTimeout(() => {
        popup.classList.remove("show");
    }, 3000);
}
