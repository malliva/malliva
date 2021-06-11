import { createSelector } from 'reselect';
import { ThunkAction } from 'redux-thunk';
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { postSignUpUser, SignUpState } from '@client/shared/account-syn-api';

export const USERS_KEY = 'signin';

export const SIGNIN_USER_KEY = 'signin';

export const initialSignInState: SignUpState = {
  first_name: '',
  last_name: '',
  username: '',
  email: '',
  password: '',
};

export const signInSlice = createSlice({
  name: SIGNIN_USER_KEY,
  initialState: initialSignInState as SignUpState,
  reducers: {
    getSignUpUserDetails: (state, action: PayloadAction<undefined>) => {
      console.log(state);
    },
  },
  //Thunk actions here
  extraReducers: {
    [postSignUpUser.fulfilled.type]: (state, action) => {
      console.log(state);
      //state.myAsyncResponse = action.payload;
    },
  },
});
// Action creators are generated for each case reducer function
export const { getSignUpUserDetails } = signInSlice.actions;

export default signInSlice.reducer;

//Gets all the state object for Users
export const getUsersState = (users: any): SignUpState => users[USERS_KEY];

// Define a thunk that dispatches those action creators
export const dispatchSignUpUser = (formData) => async (dispatch) => {
  dispatch(postSignUpUser(formData));
};
