$('.checkbox-container input').change(function () {
    let selected = [0];
    $('.checkbox-container input:checked').each(function () {
        selected.push(parseInt($(this).attr('value')));
    });
    if (selected.length > 1) {
        drawChart(selected);
    }
});

$('#fromDatepicker').datepicker({
    dateFormat: "mm/dd/yy",
    dateTimeSeparator: ", ",
    timeFormat: "hh:ii AA",
    autoClose: true,
});

$('#toDatepicker').datepicker({
    dateFormat: "mm/dd/yy",
    dateTimeSeparator: ", ",
    timeFormat: "hh:ii AA",
    autoClose: true,
    onSelect: function (fd, d, calendar) {
        //calendar.hide();
    }
});

$('#searchByDateButton').on('click', function () {
    let from = $('#fromDatepicker').val();
    let to = $('#toDatepicker').val();
    if (from && to) {
        if (new Date(from) <= new Date(to)) {
            $.ajax({
                url: appConfig.basic_url + "statistic/date",
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json',
                data: JSON.stringify({from: from, to: to}),
            }).done(function (response) {
                statisticData = response['data'];
                set_dates();
                let selected = [0];
                $('.checkbox-container input:checked').each(function () {
                    selected.push(parseInt($(this).attr('value')));
                });
                if (selected.length > 1) {
                    drawChart(selected);
                }

            });
        } else {
            alert("Second date can't be less than first!");
        }
    }
});

