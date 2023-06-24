//function filter() {
//    let pizza_objects = $(".pizza-card");
//    for (let pizza_object of pizza_objects) {
//        let data_obj = $(pizza_object).find(".pizza-data").first();
//    }
//}
//
//function search(pattern) {
//    let pizza_objects = $(".pizza-card");
//    for (let pizza_object of pizza_objects) {
//        $(".clear-link").css("display", "block");
//        let data_obj = $(pizza_object).find(".pizza-data").first();
//        $(pizza_object).css("display", "flex");
//        if (!data_obj.data("name").toUpperCase().includes(pattern)) {
//            $(pizza_object).css("display", "none");
//        }
//    }
//}

$(document).ready(() => {
    $(".navbar-invoke-block>button").click(() => {
        let collapse = $(".navbar-collapse");
        if (collapse.hasClass("class2"))
            collapse.removeClass("class2");
        else
            collapse.addClass("class2");
    });
    $(".navbar-close").click(() => {
        $("navbar-collapse").removeClass("class2")
    });
    $(".search-invoke-block").click(() => {
        $(".search-form-block").addClass("class2");
    });
    $(".search-close>button").click(() => {
        $(".search-form-block").removeClass("class2");
    });
    $(".filters-invoke-block>button").click(() => {
        $(".filters-block").addClass("class2");
    });
    $(".filters-close>button").click(() => {
        $(".filters-block").removeClass("class2");
    });

    $("a.sort-link").click((event) => {
        event.preventDefault();
        let url_params = new URLSearchParams(window.location.search);
        if ($(event.target).hasClass("clear-sort-link")) {
            if (url_params.has("order_by"))
                url_params.delete("order_by");
            return window.location.search = url_params.toString();
        }

        let k_v = $(event.target).attr("href").split("=");
        if (url_params.has(k_v[0]))
            url_params.set(k_v[0], k_v[1]);
        else
            url_params.append(k_v[0], k_v[1])
        return window.location.search = url_params.toString();
    });

    $("a.filter-link").click((event) => {
        event.preventDefault();
        let url_params = new URLSearchParams(window.location.search);
        if ($(event.target).hasClass("clear-filter-link"))
            return window.location.search = url_params.get("order_by") ? "order_by=" + url_params.get("order_by") : "";

        let k_v = $(event.target).attr("href").split("=");
        if (url_params.has(k_v[0]))
            url_params.set(k_v[0], k_v[1]);
        else
            url_params.append(k_v[0], k_v[1])
        return window.location.search = url_params.toString();
    });
//      search logic in backend now
//    $("form.search-form").submit((event) => {
//        event.preventDefault();
//        let pattern = $(event.target).find("input").first().val().toUpperCase();
//        search(pattern);
//    });
    $(".clear-link").click((event) => {
        event.preventDefault();
        let url_params = new URLSearchParams(window.location.search);
        url_params.delete('q');
        window.location.search = url_params.toString();
    });
});
