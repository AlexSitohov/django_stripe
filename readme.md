Добрый день!

Я ознакомился с официальной документацией Stripe https://stripe.com/docs и на основе этого построил свое приложение.
Я задеплоил приложение на railways по ссылке https://web-production-2697.up.railway.app/

Основной написанный мной код, находиться в приложении main. В main/views описана вся основная логика.

Логин и пароль от админки: admin и 123. Вы можете добавить новый продукт.

На главной странице приложения перечислен ассортимент товаров. Кликнув на "купить" мы попадаем на страницу с "более"
подробным видом продукта. Далее нажав на Buy срабатывает js в templates/item_detail.html на 20 строчке и перенаправляет
на форму Stripe.

Можно проверить через curl -X GET https://web-production-2697.up.railway.app/item/5/

Результатом будет 

<head>
    <title>Buy Item 5</title>
    <script src="https://js.stripe.com/v3/"></script>
</head>
<input type="hidden" name="csrfmiddlewaretoken" value="0d9kUh3UlyKihjqI14SGlZADJNEb9b2MliaEtvn5Mpjgu1EUx5lDJP9zpUIju79B">
<body>
<div style="display:flex; justify-content: space-around;">
<div class="description">
    <img src="/media/cola.jpg" style="width:300px">
    <h3>кола</h3>
    <h5>100 р.</h5>
    <h3>вкусыная</h3>
    <button type="button" id="buy-button">Buy</button>
</div>
</div>
<script type="text/javascript">
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    // Create an instance of the Stripe object with your publishable API key
    var stripe = Stripe("pk_test_51MZX2MGr1rHSHSuyTaHRmUSia2PC7icnFusl87vbm7R11C98wvL3mzjt1RFEIXAQizRWRs2oC2ruA0xmBo8zB7B200GglHP6ss");
    var buyButton  = document.getElementById("buy-button");
    buyButton.addEventListener("click", function () {
      fetch("/buy/5/", {
        method: 'GET',
        headers: {
            'X-CSRFToken': csrftoken
        }
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (session) {
          return stripe.redirectToCheckout({ sessionId: session.id });
        })
        .then(function (result) {
          // If redirectToCheckout fails due to a browser or network
          // error, you should display the localized error message to your
          // customer using error.message.
          if (result.error) {
            alert(result.error.message);
          }
        })
    });
</script>
</body>
</html>


До свидания).