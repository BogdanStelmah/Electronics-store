$("#search_user").click(function (){
   $.ajax({
      type: 'GET',
      url: 'users',
      data: {
         'first_name': $("#search_name_user").val(),
      },
      dataType: 'text',
      cache: false,
      success: function (data) {
         document.getElementById('table').remove();
            let context = JSON.parse(JSON.parse(data));

            if (context.length === 0) {
               $("#users").append("<p>Користувачів з таким ім\'ям не знайдено </p>");
            }
            else {
                showInfoUsers(context);
            }
      }
   });
});

$("#search_name_product").click(function (){
   $.ajax({
      type: 'GET',
      url: '',
      data: {
         'name': $("#search_name_product").val(),
      },
      dataType: 'text',
      cache: false,
      success: function (data) {
         document.getElementById('products').remove();
            let context = JSON.parse(JSON.parse(data));

            if (context.length === 0) {
               $("#users").append("<p>Товарів з таким ім\'ям не знайдено </p>");
            }
            else {
                showProduct(context);
            }
      }
   });
});

function showProduct(products){
   let html = ''

   for(let i = 0; i < products.length; i++){
      html += '<div>\n' +
          '<img src="photo_product/{{ p.image }}" width="100" height="100">\n' +
          '<h3>' + products[i].name + '</h3>\n' +
          '<p>' + products[i].price + ' грн</p>\n' +
          '<p>' + products[i].discounted_price + ' грн</p>\n' +
          '<p>' + products[i].categories + ' </p>\n' +
          '<pre>' + products[i].description + ' </pre>\n' +
          '</div>'
   }
}

function showInfoUsers(context) {
   let html = "<table id=\"table\">\n" +
       "                <tr>\n" +
       "                    <th>\n" +
       "                        №\n" +
       "                    </th>\n" +
       "                    <th>\n" +
       "                        Ім'я\n" +
       "                    </th>\n" +
       "                    <th>\n" +
       "                        Призвище\n" +
       "                    </th>\n" +
       "                    <th>\n" +
       "                        Логін\n" +
       "                    </th>\n" +
       "                    <th>\n" +
       "                        Пошта\n" +
       "                    </th>\n" +
       "                    <th>\n" +
       "                        Адмін\n" +
       "                    </th>\n" +
       "                </tr>"

   for (let i = 0; i < context.length; i++) {
      let superuser = '';
      if (context[i].fields.is_superuser) {
         superuser = '+'
      } else {
         superuser = "-"
      }

      html += "<tr>\n" +
          "                    <td>\n" +
          context[i].pk +
          "                    </td>\n" +
          "                    <td>\n" +
          context[i].fields.first_name +
          "                    </td>\n" +
          "                    <td>\n" +
          context[i].fields.last_name +
          "                    </td>\n" +
          "                    <td>\n" +
          context[i].fields.username +
          "                    </td>\n" +
          "                    <td>\n" +
          context[i].fields.email +
          "                    </td>\n" +
          "                    <td>\n" +
          superuser +
          "                    </td>\n" +
          "                    <td>\n" +
          "                        <a href=\"users/edit/" + context[i].pk + "\" class=\"button_edit\">Змінити</a>\n" +
          "                        <a href=\"users/delete/" + context[i].pk + "\" class=\"button_delete\">Видалити</a>\n" +
          "                    </td>\n" +
          "                </tr>"
   }
   html += "</table>\n"
   $("#users").append(html)
};