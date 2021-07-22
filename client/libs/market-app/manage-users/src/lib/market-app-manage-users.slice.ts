import { createSelector, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { getRegisteredUsers } from '@client/shared/account-syn-api';

export const USERS_KEY = 'users';

export const LIST_USER_KEY = 'users';

type ListUsersError = any;

const initialListUserState = {
  response: {},
  loading: 'idle',
  error: {},
};
export const ListUserSlice = createSlice({
  name: USERS_KEY,
  initialState: initialListUserState,
  reducers: {},
  //Thunk actions here
  extraReducers: (builder) => {
    builder.addCase(
      getRegisteredUsers.pending,
      (state, action: PayloadAction<undefined>) => {
        state.loading = 'pending';
        state.response = [];
      }
    );
    builder.addCase(getRegisteredUsers.fulfilled, (state, { payload }) => {
      state.response = payload.data;
      state.loading = 'succeeded';
      state.error = '';
    });
    builder.addCase(
      getRegisteredUsers.rejected,
      (state, action: PayloadAction<ListUsersError>) => {
        state.error = action.payload.error;
        state.loading = 'failed';
      }
    );
  },
});
// Action creators are generated for each case reducer function
export const listUserSliceReducer = ListUserSlice.reducer;

export const getListUsersState = (stateObj: any) => stateObj[LIST_USER_KEY];

export const selectListUsersStateStateLoaded = createSelector(
  getListUsersState,
  (stateObj) => stateObj
);
