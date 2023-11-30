<!DOCTYPE html>
<html>
  <head>
    <title>サイトタイトル</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="キーワード">
    <meta name="description" content="内容">
    <meta name="author" content="社名など">
    <!--sns-->
    <meta property="og:type" content="website">
    <meta property="og:description" content="キーワード">
    <meta property="og:title" content="タイトル">
    <meta property="og:image" content="og_img絶対パス">
    <meta property="og:url" content="サイトの絶対パス">
    <!--front-->
    <link href="../assets/css/common.css" rel="stylesheet">
    <script src="../assets/js/jquery-3.3.1.min.js"></script>
    <script src="../assets/js/common.js"></script>
  </head>
  <body>
    <py-script>
      import streamlit as st
      import 学校
      st.text(学校.name)
    </py-script>  
  </body>
</html>
