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
    $(this).parent().removeClass("show").hide();
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

$('.status').on('click', function () {
    let sensor_id = $(this).prop('id').replace("status", "");

    $.ajax({
        url: appConfig.basic_url + "sensor/" + sensor_id,
        type: 'PUT',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({status: $(this).data('index')}),
    }).done(function (response) {
        $('#statusDropdownMenuButton' + sensor_id).text(status_list[response['sensor']['status']]);
    });
});

$('#createSensorModalButton').click(function () {
    $('#createSensorForm').submit(function () {
        $.ajax({
            type: "POST",
            url: appConfig.basic_url + "sensor/create",
            data: $(this).serialize(),
        }).done(function () {
            window.location.reload();
        });
    }).submit();
    window.location.replace(appConfig.basic_url + "settings/sensor");
});