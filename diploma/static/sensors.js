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