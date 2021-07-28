import React from 'react';

import { MarketAppDashboardUi } from 'libs/market-app/dashboard/dashboard-ui/src/index';
import { MarketAppManageUsers } from 'libs/market-app/manage-users/src/index';
import { MarketAppDashboardDashboardMenu } from 'libs/market-app/dashboard/dashboard-menu/src/index';

import { MarketAppUserFields } from 'libs/market-app/user-fields/src/index';
import { MarketAppUserRights } from 'libs/market-app/user-rights/src/index';

import { MarketAppTopMenu } from '@client/market-app/top-menu';
import { Redirect, Route, Switch } from 'react-router-dom';

/* eslint-disable-next-line */
export interface MarketAppDashboardProps {}

export function MarketAppDashboard({ match }) {
  const userNavigation = [{ name: 'Admin panel', href: '#', type: 'admin' }];

  return (
    <Switch>
      {match.params.slug === 'manage-users' && (
        <Route path={`${match.url}`}>
          <MarketAppTopMenu menu={userNavigation} {...match} />
          <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
            <MarketAppDashboardDashboardMenu />
            <MarketAppManageUsers />
          </div>
        </Route>
      )}
      {match.params.slug === 'users-rights' && (
        <Route path={`${match.url}`}>
          <MarketAppTopMenu menu={userNavigation} {...match} />
          <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
            <MarketAppDashboardDashboardMenu />
            <MarketAppUserRights />
          </div>
        </Route>
      )}
      {match.params.slug === 'users-fields' && (
        <Route path={`${match.path}`}>
          <MarketAppTopMenu menu={userNavigation} {...match} />
          <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
            <MarketAppDashboardDashboardMenu />
            <MarketAppUserFields />
          </div>
        </Route>
      )}

      <Route path={`/dashboard/index`}>
        <MarketAppTopMenu menu={userNavigation} {...match} />
        <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
          <MarketAppDashboardDashboardMenu />
          <MarketAppDashboardUi />
        </div>
      </Route>
      {/* Fixes signout in dashboard */}
      {match.params.slug === 'sign-out' && <Redirect to="/sign-out" />}

      <Redirect to="/index" />
    </Switch>
  );
}

export default MarketAppDashboard;
