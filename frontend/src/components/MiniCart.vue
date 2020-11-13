<template>
    <v-container>
        <v-card>
            <v-card-title>Shopping Cart</v-card-title>
            <v-card-text>
                <div v-for="item in Cart" :key="item.Product.id">
                    <div>{{ item.Product.title }}</div>
                    <div>{{ item.Product.price }}</div>
                </div>
                   
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>

export default {
    computed: {
        Cart(){
            return this.$store.state.Cart;
        }
    }
}
</script>