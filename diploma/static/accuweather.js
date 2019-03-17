async function get_region_info(lat, long) {
    let result = "0";
    const params = {apikey: appConfig.api_key, q: lat + "," + long};
    await $.get(appConfig.accu_basic_url + "locations/v1/cities/geoposition/search", params, function (data) {
        console.log(data['Key']);
        result = data;
    }, "json");
    return result;
}

async function get_1hour_forecast(regionKey) {
    let result = "0";
    const params = {apikey: appConfig.api_key, lanuage: appConfig.language, metric: true};
    const url = "forecasts/v1/hourly/1hour/" + regionKey;
    await $.get(appConfig.accu_basic_url + url, params, function (data) {
        console.log(data);
        console.log(data[0]['Temperature']);
        result = data[0]['Temperature'];
    }, "json");
    return result;
}