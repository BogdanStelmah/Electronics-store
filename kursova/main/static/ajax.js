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

$("#search_product").click(function (){
   $("#add_product").attr('count_show', "4")

   $.ajax({
      type: 'GET',
      url: '',
      data: {
         'search': $("#search_name_product").val(),
         'category': get_arr_checkbox(),
         'price__from': $("#price__from").val(),
         'price__to': $("#price__to").val(),

         'count_show': 2
      },
      dataType: 'text',
      cache: false,
      success: function (data) {
         document.getElementById('products').textContent = '';
         let context = JSON.parse(JSON.parse(data));

         if (context.length === 0) {
            $("#products").append("<p>Товарів з таким ім\'ям не знайдено </p>");
         }
         else {
            showProduct(context);
         }
      }
   });
});

$("#filter").click(function (){
   $("#add_product").attr('count_show', "4")

   $.ajax({
      type: 'GET',
      url: '',
      data: {
         'category': get_arr_checkbox(),
         'price__from': $("#price__from").val(),
         'price__to': $("#price__to").val(),

         'count_show': 2
      },
      dataType: 'text',
      cache: false,
      success: function (data) {
         document.getElementById('products').textContent = '';
         let context = JSON.parse(JSON.parse(data));

         if (context.length === 0) {
            $("#products").append("<p>Товарів з таким ім\'ям не знайдено </p>");
         }
         else {
            console.log(context)
            showProduct(context);
         }
      }
   });
});

$("#add_product").click(function (){
   let btn_more = $(this);
   let count_show = parseInt($(this).attr('count_show'));
   let count_add  = parseInt($(this).attr('count_add'));

   $.ajax({
      type: 'GET',
      url: '',
      data: {
         'search': $("#search_name_product").val(),
         'category': get_arr_checkbox(),
         'price__from': $("#price__from").val(),
         'price__to': $("#price__to").val(),

         'count_show': count_show
      },
      dataType: 'text',
      cache: false,
      success: function (data) {
         btn_more.attr('count_show', (count_show+count_add));

         document.getElementById('products').textContent = '';

         let context = JSON.parse(JSON.parse(data));

         if (context.length === 0) {
            $("#products").append("<p>Товарів з таким ім\'ям не знайдено </p>");
         }
         else {
            showProduct(context);
         }
      }
   });
})

function get_arr_checkbox(){
   let checkbox = document.getElementsByClassName('filter_checkbox')
   let arr_checkbox = [];
   for (let i = 0; i < checkbox.length; i++){
      if (checkbox[i].checked){
         arr_checkbox.push(checkbox[i].value)
      }
   }

   return arr_checkbox
}

function showProduct(products){
   let html = ''

   for(let i = 0; i < products.length; i++){
      let number = ''
      if ( products[i].fields.number === 0){
         number = '<p class="product__number">Немає в наявності</p>';
      }

      let discount = ''
      if (products[i].fields.discount !== 0){
         discount = '<div class="product__price__old">\n' +
          '          <s><p>'+ products[i].fields.price +' грн</p></s>\n' +
          '          <span class="product__discount">\n' +
          '          -'+ products[i].fields.discount +'%\n' +
          '          </span>\n' +
          '          </div>\n' +
          '          <p class="product__price">'+ products[i].fields.discounted_price +' грн</p>\n'
      }
      else {
         discount = '<p>'+ products[i].fields.price +' грн</p>';
      }
      html += '<div class="items__product">\n' +
          '                        <a href="product/'+ products[i].pk +'/"><img src="photo_product/'+ products[i].fields.image + '" width="100" height="100"></a>\n' +
          '                        <div class="product__info">\n' +
          '                            <h3>'+ products[i].fields.name +'</h3>\n' +
          '                            <div class="product__price">\n' +
          '                                <div class="info">\n' + number +
          '                                    <div class="block__basket__and__price">\n' +
          '                                        <div>\n' + discount +
          '                                        </div>\n' +
          '                                        <a href="add_item_basket/'+ products[i].pk + '/"><img src="/static/img/cart.png" class="basket"></a>\n' +
          '                                    </div>\n' +
          '                                </div>\n' +
          '                            </div>\n' +
          '                        </div>\n' +
          '                    </div>'
   }
   $("#products").append(html);
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