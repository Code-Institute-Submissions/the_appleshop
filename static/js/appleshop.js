$(document).ready(function(){

});

// show delete recipe confirmation popup
function showdeleteReviewPopup() {
    $('#deletePopup').css("transform", "translateX(0vw)");

    $('#deletePopup').css("opacity", "1.0");
}

// cancel delete recipe button
function cancelDeleteReview() {
    $('#deletePopup').css("opacity", "0.0");
    setTimeout(function () {
        $('#deletePopup').css("transform", "translateX(-100vw)");
    }, 400);
}

function sendDeleteForm() {
    $('#deletePopupForm').submit();
}