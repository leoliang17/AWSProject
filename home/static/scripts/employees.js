$(document).ready(function(){
    // Activate the data table and provide confirm box deleting products
    $('#sort').dataTable({
        "columnDefs": [
            { "orderable": false, "targets": 5 }
        ]
    });

    $('.delete_btn').click(function() {
        if (confirm("Are you sure you want to delete this product?")) {}
        else {return false}
    })

});