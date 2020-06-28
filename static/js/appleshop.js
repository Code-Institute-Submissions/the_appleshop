$(document).ready(function () {

});

function showDeletePopup() {
    $('#freeShippingPopup').css("transform", "translateZ(400px)").css("z-index", "400");
    setTimeout(function() {
        $('#freeShippingPopup').css("opacity", "1.0");
    }, 300);
}

function closeDeletePopup(){
    $('#freeShippingPopup').css("opacity", "0.0");
    setTimeout(function() {
        $('#freeShippingPopup').css("transform", "translateZ(-10px)").css("z-index", "-1");
    }, 700);
}