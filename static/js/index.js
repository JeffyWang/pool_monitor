
    $.ajax({
        url: '/monitor',
        type: "GET",
        dataType: "json",
        contentType: 'application/json;charset=utf-8',
        success: function (data) {
            console.log(data)
        }
    })