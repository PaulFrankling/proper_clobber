// Country Field JS for Profile page
let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#7E7F83');
}
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#7E7F83');
    } else {
        $(this).css('color', '#000000');
    }
});