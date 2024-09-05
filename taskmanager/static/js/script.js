document.addEventListener('DOMContentLoaded', function() {

    // sidnav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialization
    let datePicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datePicker, {format:"dd mmmm, yyyy", i18n: {done:"Select"}});

    // select initialization
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    // collapsible initialization
    let collaps = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collaps);
  });

  