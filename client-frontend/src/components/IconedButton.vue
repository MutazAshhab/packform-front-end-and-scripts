<template>
    <button>
        <i :class="'fas ' + icon"></i>
        {{ text }}
    </button>
</template>

<script>
export default {
    name: 'IconedButton',
    props: {
        text: String,
        icon: String,
    },
};
</script>

<style scoped>
button {
    background-color: white;
    border-radius: 5px;
    border: transparent;
}
button:hover {
    transition: 500ms;
    cursor: pointer;
    background-color: #dcdcdc;
}
</style>
