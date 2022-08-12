



var currentDiv = document.getElementById('pizza-menu');
var nr = 0;

function showMe(divName){
   var div = document.getElementById(divName);

   if(div.style.display == 'none'){
        div.style.display = 'block';
                currentDiv.style.display = 'none';

        this.currentDiv = document.getElementById(divName);

   }
   else {
        div.style.display = 'none';
                currentDiv.style.display = 'block';

        this.currentDiv = document.getElementById(divName);

   }
}

function hideImg(){
    var div = document.getElementById('full-image');
    div.style.display = 'none';
}

function showImg(chooseNumber){
    var div = document.getElementById('full-image');
    div.style.display = 'block';
    nr = chooseNumber
}

function choose(){
    return nr;
}


var zoomImg = function () {
  // (A) CREATE EVIL IMAGE CLONE
  var clone = this.cloneNode();
  clone.classList.remove("zoomD");

  // (B) PUT EVIL CLONE INTO LIGHTBOX
  var lb = document.getElementById("lb-img");
  lb.innerHTML = "";
  lb.appendChild(clone);

  // (C) SHOW LIGHTBOX
  lb = document.getElementById("lb-back");
  lb.classList.add("show");
};

window.addEventListener("load", function(){
  // (D) ATTACH ON CLICK EVENTS TO ALL .ZOOMD IMAGES
  var images = document.getElementsByClassName("zoomD");
  if (images.length>0) {
    for (var img of images) {
      img.addEventListener("click", zoomImg);
    }
  }

  // (E) CLICK EVENT TO HIDE THE LIGHTBOX
  document.getElementById("lb-back").addEventListener("click", function(){
    this.classList.remove("show");
  })
});