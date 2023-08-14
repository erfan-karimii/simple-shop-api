<template>
    <div class="success-page">
        <div class="columns is-muitline">
            <div class="column is-12">
                <h1 class="title">Thank You</h1>
                <p>Your order will be processed ready within 48 hour</p>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name:'Success',
    mounted(){
        document.title = 'success | bookstore'
    }
}
</script>