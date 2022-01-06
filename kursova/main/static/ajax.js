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
         let context = JSON.parse(JSON.parse(data))

         document.getElementById('table').remove()

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

         for (let i = 0; i < context.length; i++){
            let superuser = '';
            if (context[i].fields.is_superuser){
               superuser = '+'
            }
            else {
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
                "                        <a href=\"users/edit/"+ context[i].pk +"\" class=\"button_edit\">Змінити</a>\n" +
                "                        <a href=\"users/delete/"+ context[i].pk +"\" class=\"button_delete\">Видалити</a>\n" +
                "                    </td>\n" +
                "                </tr>"
         }
         html += "</table>\n"
         $("#users").append(html)
      }
   });
});