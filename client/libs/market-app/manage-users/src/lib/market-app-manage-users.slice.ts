import { createSelector, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { getRegisteredUsers } from '@client/shared/account-syn-api';

export const USERS_KEY = 'users';

export const MANAGE_USERS_KEY = 'users';

type ManageUsersError = any;

const initialManageUserState = {
  response: {},
  loading: 'idle',
  error: {},
};
export const ListUserSlice = createSlice({
  name: USERS_KEY,
  initialState: initialManageUserState,
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
      (state, action: PayloadAction<ManageUsersError>) => {
        state.error = action.payload.error;
        state.loading = 'failed';
      }
    );
  },
});
// Action creators are generated for each case reducer function
export const manageUserSliceReducer = ListUserSlice.reducer;

export const getManageUsersState = (stateObj: any) =>
  stateObj[MANAGE_USERS_KEY];

export const selectListUsersStateStateLoaded = createSelector(
  getManageUsersState,
  (stateObj) => stateObj
);
