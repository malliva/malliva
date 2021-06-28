import { render } from '@testing-library/react';

import MarketAppDashboardDashboardMenu from './market-app-dashboard-dashboard-menu';

describe('MarketAppDashboardDashboardMenu', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppDashboardDashboardMenu />);
    expect(baseElement).toBeTruthy();
  });
});
