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
    $("#delete-context-menu").css({
        display: "block",
        top: top,
        left: left
    }).addClass("show");
    return false; //blocks default Webbrowser right click menu
}).on("click", function () {
    $("#delete-context-menu").removeClass("show").hide();
});

$("#delete-context-menu a").on("click", function () {
    //;alert(sensor.getAttribute("id"));
    $(this).parent().removeClass("show").hide();
});

$(document).ready(function () {
    $('#deleteSensorModal').on('show.bs.modal', function () {
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        let modal = $(this);
        //modal.find("#exampleModalLongTitle").text(sensor.childNodes[1].textContent);
    });
});

$('#deleteSensorModalButton').click(function () {
    $.ajax({
        url: appConfig.basic_url + "sensor/" + sensor.getAttribute('id').replace("sensor", ""),
        type: 'DELETE',
    }).done(function () {
        sensor.remove();
    });
});

$('.is_shared').change(function () {
    $.ajax({
        url: appConfig.basic_url + "sensor/" + $(this).prop('id').replace("is_shared", ""),
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify({is_shared: $(this).prop('checked')}),
    }).done(function () {

    });
});

$('.sync_type').on('click', function () {
    let sensor_id = $(this).prop('id').replace("sync_type", "");
    //alert($(this).text())
    $.ajax({
        url: appConfig.basic_url + "sensor/" + sensor_id,
        type: 'PUT',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({sync_type: $(this).data('index')}),
    }).done(function (response) {
        $('#sync_typeDropdownMenuButton' + sensor_id).text(sync_type_list[response['sensor']['sync_type']]);
    });
});
