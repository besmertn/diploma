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
    dateFormat: "m/d/yy",
    dateTimeSeparator: ", ",
    timeFormat: "hh:ii AA",
    autoClose: true,
    onSelect: function (fd, d, calendar) {
        //calendar.hide();
    }
});

$('#toDatepicker').datepicker({
    dateFormat: "m/d/yy",
    dateTimeSeparator: ", ",
    timeFormat: "hh:ii AA",
    autoClose: true,
    onSelect: function (fd, d, calendar) {
        //calendar.hide();
    }
});

