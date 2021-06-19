<template>
    <div class="top-bar">
        <img class="top-bar-img" alt="Vue logo" src="../assets/logo.png">
        <h1>Realtime Markers</h1>
        <h3>{{message}}</h3>
    </div>
</template>

<script>
export default {
    props: {
        message: String,
    }  
}
</script>

<style scoped>
    .top-bar{
        position: absolute;
        top: 0px;
        left: 0px;
        width: 100%;
        height: 50px;
        background: rgb(32, 138, 165);
        display: flex;
        align-items: center;
        color: white;
    }
    
    .top-bar-img{
        width: 50px;
        height: 50px;
        margin-left: 25px;
        margin-right: 25px;
    }
    .top-bar h3{
        position: absolute;
        right: 0px;
        margin-right: 25px;
    }
</style>