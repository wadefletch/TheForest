function update() {
    $.get("/_actions", function(data) {
        $("#actions-frame").html(data);
    })
    $.get("/_events", function(data) {
        $("#events-frame").html(data);
    })
    $.get("/_inventory", function(data) {
        $("#inventory-frame" ).html(data);
    });

}

var interval = self.setInterval(function(){update()},2000);