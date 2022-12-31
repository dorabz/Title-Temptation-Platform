<template>
<footer class="footer">
    <div class="container">
      <div class="content has-text-centered">
        <p>
            Ⓒ Title Temptation
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
    export default {
        name: 'Footer'
    }
</script>

<style scoped>
footer{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
    background-color: #041220;
    color: white;
    font-family: 'Trebuchet Ms', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-size: 90%;
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 50px; /* Set this to the height of your footer */
}
.content {
    color: white;
}
</style>