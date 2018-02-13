var btn = document.getElementById('btn');
btn.addEventListener("click", function() {
    var myCount = this.innerHTML;
    btn.innerHTML = parseInt(myCount)+1;
});

