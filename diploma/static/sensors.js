async function getSensorsByRegionKey(regionKey) {
    let result = "0";
    await $.get(appConfig.basic_url + "sensor/region/" + regionKey, function (data) {
        console.log(data);
        result = data['sensors'];
    }, "json");
    return result;
}

let instance = OverlayScrollbars(document.getElementById('sensors_table'), {
    scrollbars: {
        visibility: "auto",
        autoHide: "leave",
        autoHideDelay: 800,
        dragScrolling: true,
        clickScrolling: false,
        touchSupport: true
    },
});


let sensor;

$('.sensor').on('contextmenu', function (e) {
    sensor = this;
    let top = e.pageY - 10;
    let left = e.pageX - 90;
    $("#context-menu").css({
        display: "block",
        top: top,
        left: left
    }).addClass("show");
    return false; //blocks default Webbrowser right click menu
}).on("click", function () {
    $("#context-menu").removeClass("show").hide();
});

$("#context-menu a").on("click", function () {
    //;alert(sensor.getAttribute("id"));
    $(this).parent().removeClass("show").hide();
});

$(document).ready(function () {
    $('#exampleModalCenter').on('show.bs.modal', function () {
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        let modal = $(this);
        modal.find("#exampleModalLongTitle").text(sensor.childNodes[1].textContent);
    });
});
