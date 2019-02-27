async function get_location_key(lat, long) {
        var result = "0";
        var params = {apikey: appConfig.api_key, q: lat + "," + long};
        await $.get(appConfig.basic_url + "locations/v1/cities/geoposition/search", params, function (data) {
            console.log(data['Key']);
            result = data['Key'];
        }, "json");
        return result;
    }

    async function get_1hour_forecast(lat, long) {
        var params = {apikey: appConfig.api_key, lanuage: appConfig.language};
        var url = "forecasts/v1/hourly/1hour/" + await get_location_key(lat, long);
        $.get(appConfig.basic_url + url, params, function (data) {
            console.log(data);
            console.log(data[0]['Temperature']);
            return data['Temperature'];
        }, "json")
    }