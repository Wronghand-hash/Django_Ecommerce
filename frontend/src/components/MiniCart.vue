<template>
    <v-container>
        <v-card>
            <v-card-title>Shopping Cart</v-card-title>
            <v-card-text>
                <div v-for="item in cart" :key="item.product.title">
                    <div>{{ item.product.title }}</div>
                </div>

            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>

export default {
    computed: {
        cart(){
            return this.$store.state.cart;
        }
    }
}
</script>