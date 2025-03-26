<!DOCTYPE html>
<html>
  <head>
    <title>Wedding</title>
    <style>
      body {
        margin: 0px;
        padding: 0px;
      }
      .wedding1jpg {
        height: 735px;
      }
      .p1 {
        display: block;
        font-size: 50px;
        color: #ADC29B;
      }
      .flex1 {
        display: flex;
        width: 800px;
        justify-content: space-between;
        align-items: center;
      }
      .flex11 {
        display: flex;
      }
      .flex12 {
        display: flex;
      }
      .flex13 {
        display: flex;
      }
      .p2:hover {
        text-decoration: underline;
      }
      .first-page {
        display: grid;
        grid-template-columns: 600px 1fr;
      }
    </style>
  </head>
  <body>
    <div class="first-page">
      <div style="">
        <img style="height: 735px; padding-right: 0px;" src="wedding1.jpg">
      </div>
      <div>
        <p class="p1">Blissify</p>
      <div class="flex1">
        <div class="flex11">
          <button style="height: 25px; margin-top: 13px; margin-right: 5px;">1</button>
          <p>Get started</p>
        </div>
        <div class="flex12">
          <button style="height: 25px; margin-top: 13px; margin-right: 5px;">2</button>
          <p>More information</p>
        </div>
        <div class="flex13">
          <button style="height: 25px; margin-top: 13px; margin-right: 5px;">3</button>
          <p>Finish up</p>
        </div>
      </div>
      <p style="font-weight: bold; font-size: 30px;">Follow these simple steps to get  started</p>
      <div style=
      "display: grid;
      grid-template-columns: 200px 200px;
      ">
        <div>
          <p style="margin-bottom: 5px;">Fisrt name</p>
          <input type="text">
        </div>
        <div>
          <p style="margin-bottom: 5px;">Last name</p>
          <input type="text">
        </div>
        
        <div>
          <p style="margin-bottom: 5px;">Partner's first name</p>
          <input type="text">
        </div>
        <div>
          <p style="margin-bottom: 5px;">Partner's last name</p>
          <input type="text">
        </div>
      </div>
      <p>Wedding date <span style="color: gray;">(Don't worry! You can change this later)</span> </p>
      <div style=
      "display: flex;
      flex-direction: row;
      width: 800px;
      "
      >
        <div>
          <input type="date" style="font-size: 20px; margin-right: 35px;">
        </div>
        <div>
          <input type="checkbox" style="width: 15px;  margin-right: 7px; height: 25px;">
        </div>
        <div>
          <p style="margin-top: 5px;">We're still deciding</p>
        </div>
      </div>
      <button style="background-color: lightgreen; width: 400px; font-size: 20px; border: 1px solid gray; border-radius: 15px; padding: 5px">
    
        Next
      </button>
      <p>Already have an account? <strong><span class="p2">Log in </span> </strong> </p>
        </div>
    </div>
    <script>

    </script>
  </body>
</html>