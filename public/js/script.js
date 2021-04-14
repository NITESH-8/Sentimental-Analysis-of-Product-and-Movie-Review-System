const commentBtn = document.querySelector(".comment-btn");
const urlBtn = document.querySelector(".url-btn");
const clearBtn = document.querySelector(".clear-btn");
console.log("STARTED");
function showResult(res) {
    console.log("DISPLAYING RESULT!");
    let result = res.slice(res.search(":") + 2, res.search(",")); //post negt
    let per = res.slice(res.search("Probability: ") + 13);
    document.querySelector(".resultcom").innerText = result.toUpperCase();
    document.querySelector(".resultper").innerText = per;
    document.querySelector(".resultimg").classList = ["resultimg"]
    document.querySelector(".resultimg").classList.add(result.slice(0, 3))
}

function processAnimate() {
    console.log("PROCESSING....");
    document.querySelector(".resultimg").classList = ["resultimg"]
    document.querySelector(".resultcom").innerText = "Processing.."
    document.querySelector(".resultper").innerText = "--%";
    document.querySelector(".resultimg").classList.add("loader");
}

function commentBtnClicked() {
    console.log("COMMENT BUTTON CLICKED");
    let comment = document.getElementsByName('comment')[0].value;
    console.log(comment);

    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (this.readyState == 1) {
            processAnimate();
        }
        if (this.readyState == 4) {
            let res = this.responseText;
            document.querySelector(".resultimg").classList.remove("loader");
            showResult(res);
        }
    }
    xhr.open("POST", "/", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({
        comment: comment,
        url: '',
    }));
}

function urlBtnClicked() {
    console.log("URL BUTTON CLICKED");
    let url = document.getElementsByName('url')[0].value;
    console.log(url);
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        console.log(this.readyState);
        if (this.readyState == 1) {
            processAnimate();
        }
        if (this.readyState == 4) {
            let res = this.responseText;
            document.querySelector(".resultimg").classList.remove("loader");
            showResult(res);
        }
    }
    xhr.open("POST", "/", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({
        comment: '',
        url: url,
    }));
}

function clearInputFields() {
    document.getElementsByName('comment')[0].value = ""
    document.getElementsByName('url')[0].value = ""
    document.querySelector(".resultimg").classList = ["resultimg"]
    document.querySelector(".resultcom").innerText = "RESULT"
    document.querySelector(".resultper").innerText = "--%";
}

commentBtn.addEventListener("click", commentBtnClicked);
urlBtn.addEventListener("click", urlBtnClicked);
clearBtn.addEventListener("click", clearInputFields);