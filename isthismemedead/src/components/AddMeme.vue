<template>
  <div>
  <el-button icon="el-icon-plus" type="primary"  @click="centerDialogVisible = true" round>
    ADD A MEME
  </el-button>
  <el-dialog
    title="Add a meme"
    :visible.sync="centerDialogVisible"
    width="30%"
    center>
    <span>To add a meme you must take the link from <a href="https://knowyourmeme.com">Know Your Meme</a></span>
    <el-form :model="form" :rules="rulesLink" ref="form">
      <el-form-item label="Link" prop="link">
        <el-input suffix-icon="" placeholder="exemple : https://knowyourmeme.com/memes/annoyed-bird" v-model="form.link" autocomplete="off"></el-input>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
    <el-button @click="centerDialogVisible = false">Cancel</el-button>
    <el-button type="primary" @click="submitForm('form')">Confirm</el-button>
  </span>
  </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios';

export default {
  name: 'AddMeme',
  data() {
    const checkLink = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please input the link'));
      }
      const re = new RegExp('^(http:\\/\\/www\\.|https:\\/\\/www\\.|http:\\/\\/|https:\\/\\/)?[a-z0-9]+([\\-\\.]{1}[a-z0-9]+)*\\.[a-z]{2,5}(:[0-9]{1,5})?(\\/.*)?$');
      if (!value.match(re)) {
        callback(new Error('Please enter a correct link format'));
      } else if (value.search('knowyourmeme.com') <= 0) {
        callback(new Error('Please enter a knowyourmeme.com link'));
      } else {
        callback();
      }
    };
    return {
      centerDialogVisible: false,
      form: {
        link: '',
      },
      rulesLink: {
        link: [
          { validator: checkLink, trigger: 'blur' },
        ],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.centerDialogVisible = false;
          this.openMessage('Thank you for your submission, your meme will be added soon', 'success');
          return true;
        }
        // this.openMessage('An Unexpected Error Occurred', 'error');
        return false;
      });
    },
    openMessage(message, type) {
      this.$message({
        message,
        type,
      });
    },
  },
};
</script>

<style scoped>

</style>
