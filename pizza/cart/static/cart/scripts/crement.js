$(document).ready(() => {
    $('form.decrement-form').submit((event) => {
        event.preventDefault();
        let form = $(event.target);
        let p = form.siblings('p');
        if (p.text() <= 1)
            return
        p.text(Number(p.text()) - 1);

        let data = form.serialize();
        $.ajax({
            type: "post",
            url: form.attr('action'),
            data: {
                'csrfmiddlewaretoken': data.split("=")[1]
            },
            success: function (response) {
                console.log('OK -');
            }
        });
    });
    $('form.increment-form').submit((event) => {
        event.preventDefault();
        let form = $(event.target);
        let p = form.siblings('p');
        p.text(Number(p.text()) + 1);

        let data = form.serialize();
        $.ajax({
            type: "post",
            url: form.attr('action'),
            data: {
                'csrfmiddlewaretoken': data.split("=")[1]
            },
            success: function (response) {
                console.log('OK +');
            }
        });
    });
});