$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').on('click', () => {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), data => {
      $('DIV#hello').text(data.hello);
    });
  });
});
