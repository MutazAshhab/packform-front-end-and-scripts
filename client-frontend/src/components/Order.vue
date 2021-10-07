<template>
    <td>{{ order.OrderName }}</td>
    <td>{{ order.CustomerCompany }}</td>
    <td>{{ order.CustomerName }}</td>
    <td>{{ order.CreatedAt }}</td>
    <td>{{ order.DeliveredAmount }}</td>
    <td>{{ order.TotalAmount }}</td>
</template>

<script>
export default {
    name: 'Order',
    props: {
        order: Object,
    },
};
</script>

<style scoped>
td {
    padding: 5px;
}
</style>
